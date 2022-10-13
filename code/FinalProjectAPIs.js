const mysql = require('mysql2');

const pool = mysql.createPool({
    host: "localhost",
    user: "root",
    password: "abc",
    database: "mydb",
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

const express = require('express')
const app = express()
const port = 3000

app.use(express.json())

//GET: Reports based on UserID and Access Restrictions
app.get('/user/:uid', (req, res, fields) => {
    pool.query(`SELECT * from users WHERE UserID=?`, [`${req.params.uid}`], function (err, result, fields) {
        if (err) throw err;
        role = result[0]['RoleID'];  
        //Admins can view all courses
        if (role == 1) {
            pool.query(`SELECT * FROM courses`, function (err, result, fields) {
                if (err) throw err;   
                 res.send(result);   
              } );
        }
        //List of Teachers Assigned Courses
        else if (role == 2) {
            pool.query(`SELECT courses.Title, users.Name 
            FROM courses
            LEFT JOIN users
            ON courses.TeacherID = users.UserID
            WHERE users.UserID=?`, [`${req.params.uid}`], function (err, result, fields) {
                if (err) throw err;   
                 res.send(result);   
              } );
        }
        //List of Students Grades
        else if (role == 3) {
            pool.query(`SELECT users.Name, courses.Title, enrolments.Mark
            FROM users
            INNER JOIN enrolments 
            ON users.UserID = enrolments.UserID
            INNER JOIN courses 
            ON enrolments.CourseID = courses.CourseID
            WHERE users.UserID=?`, [`${req.params.uid}`], 
            function (err, result, fields) {
                if (err) throw err;                 
                 res.send(result);   
              } );
        }
    }) 
  });



  


//UPDATE: 1) Admin Change Course Availability  
app.patch('/course/availability/:cid/user/:uid', (req, res) => {
    pool.query(`SELECT * from users WHERE UserID=?`, [`${req.params.uid}`], function (err, result, fields) {
        if (err) throw err;
        role = result[0]['RoleID'];  
        if (role == 1) {
            const isavailable = req.body.isAvailable
            pool.query(`UPDATE courses SET isAvailable=? WHERE CourseID=?`, [`${isavailable}`, `${req.params.cid}`], 
            function (err, result, fields) {
                if (err) throw err;   
                 res.send(`Course ${req.params.cid} has been updated!`);   
              });
        }
        else {
            res.send("Access Denied")
        };
    }) 
});

//UPDATE: 2) Admin Assign Courses to Teachers 
app.patch('/course/teacher/:cid/user/:uid', (req, res) => {
    pool.query(`SELECT * from users WHERE UserID=?`, [`${req.params.uid}`], function (err, result, fields) {
        if (err) throw err;
        role = result[0]['RoleID'];  
        if (role == 1) {
            const teacher = req.body.TeacherID
            pool.query(`UPDATE courses 
            SET TeacherID=? 
            WHERE CourseID=?`, [`${teacher}`, `${req.params.cid}`], 
            function (err, result, fields) {
                if (err) throw err;   
                 res.send(`Course ${req.params.cid} assigned to teacher ${teacher}`);   
              });
        }
        else {
            res.send("Access Denied")
        };
    }) 
});
//GET: 3) Studnets Can View Available Courses
app.get('/available/courses/user/:uid', (req, res) => {
    pool.query(`SELECT * from users WHERE UserID=?`, [`${req.params.uid}`], function (err, result, fields) {
        if (err) throw err;
        role = result[0]['RoleID'];  
        if (role == 3) {
            pool.query(`SELECT courses.Title, users.Name
            FROM courses
            INNER JOIN users 
            ON courses.TeacherID = users.UserID
            WHERE isAvailable=1;`, (err, result, fields)=> {
                if (err) throw err;
                res.send(result);

            });
        }
        else {
            res.send("Access Denied")
        };
    })
});


//UPDATE: 4) Students Enrolment to Courses
app.post('/enrol/add/user/:uid', (req, res) => {
    pool.query(`SELECT * from users WHERE UserID=?`, [`${req.params.uid}`], function (err, result, fields) {
        if (err) throw err;
        role = result[0]['RoleID'];  
        if (role == 3) {
            const courseid = req.body.CourseID
            pool.query(`SELECT * FROM enrolments WHERE UserID=? AND CourseID=?`, 
                [`${req.params.uid}`, `${courseid}`], (err, result, fields)=> {
                    if (result.length){
                        res.send("You are already enroled!")
                    }else{
                        pool.query(`INSERT INTO enrolments 
                        SET UserID=?, CourseID=?`, [`${req.params.uid}`, `${courseid}`],
                        function (err, result, fields) {
                            if (err) throw err;
                            res.send('Congradulations you have successfully enrolled!')
                        });
                    }
                });
        }
        else {
            res.send("Access Denied")
        };
    }) 
});

//UPDATE: 5) Teacher Pass/Fail Students
app.patch("/course/mark/user/:uid",  (req, res) => {
    pool.query(`SELECT * FROM users WHERE UserID=?`, [`${req.params.uid}`], (err, result, fields) => {
        if (err) throw err;
        role = result[0]['RoleID']
        if (role == 2) {
            const mark = req.body.Mark
            const courseid = req.body.CourseID
            const studentid = req.body.UserID
            pool.query(`SELECT * FROM enrolments 
            WHERE CourseID=? AND UserID=?`, [`${courseid}`,`${studentid}`],
            (err, result, fields) => {
                if (!result.length) {
                    res.send("This entry does not exist or StudentID/CourseID are incorrect")
                }else{
                    pool.query(`UPDATE enrolments 
                    SET Mark=?
                    WHERE CourseID=? AND UserID=?;`, [`${mark}`,`${courseid}`,`${studentid}`],
                    (err, result, fields) => {
                        if (err) throw err;
                        res.send("Mark has been entered successfuly")
                    });
                }
            })
        }
        else {
            res.send("Access Denied")
        };
    })
});

app.listen(port, () => {
    console.log(`API connected on port ${port}`)
});