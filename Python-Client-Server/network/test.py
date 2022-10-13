"""
Test module client-server connection
"""

import unittest, socket
from encrypt import *
from pickling import *

class test_encryptions(unittest.TestCase):
    def test_reading(self):
        self.assertEqual(read_file("./testing_file.txt"), b'Hello, world!')

class test_pickling(unittest.TestCase):
    def test_json(self):
        self.assertEqual(to_json({
                "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
                "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
                "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
                "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110}
                }), 
                b'{"Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110}, "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110}, "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93}, "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110}}')

    def test_xml(self):
        self.assertEqual(to_xml({
                "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
                "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
                "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
                "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110}
                }), 
                b'<?xml version="1.0" encoding="UTF-8" ?><root><Mazda_RX4 type="dict"><mpg type="int">21</mpg><cyl type="int">6</cyl><disp type="int">160</disp><hp type="int">110</hp></Mazda_RX4><Mazda_RX4_Wag type="dict"><mpg type="int">21</mpg><cyl type="int">6</cyl><disp type="int">160</disp><hp type="int">110</hp></Mazda_RX4_Wag><Datsun_710 type="dict"><mpg type="float">22.8</mpg><cyl type="int">4</cyl><disp type="int">108</disp><hp type="int">93</hp></Datsun_710><Hornet_4_Drive type="dict"><mpg type="float">21.4</mpg><cyl type="int">6</cyl><disp type="int">258</disp><hp type="int">110</hp></Hornet_4_Drive></root>')

    def test_binary(self):
        self.assertEqual(to_bin({
                "Mazda RX4": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
                "Mazda RX4 Wag": {"mpg": 21, "cyl": 6, "disp": 160, "hp": 110},
                "Datsun 710": {"mpg": 22.8, "cyl": 4, "disp": 108, "hp": 93},
                "Hornet 4 Drive": {"mpg": 21.4, "cyl": 6, "disp": 258, "hp": 110}
                }), b'1111011 100010 1001101 1100001 1111010 1100100 1100001 100000 1010010 1011000 110100 100010 111010 100000 1111011 100010 1101101 1110000 1100111 100010 111010 100000 110010 110001 101100 100000 100010 1100011 1111001 1101100 100010 111010 100000 110110 101100 100000 100010 1100100 1101001 1110011 1110000 100010 111010 100000 110001 110110 110000 101100 100000 100010 1101000 1110000 100010 111010 100000 110001 110001 110000 1111101 101100 100000 100010 1001101 1100001 1111010 1100100 1100001 100000 1010010 1011000 110100 100000 1010111 1100001 1100111 100010 111010 100000 1111011 100010 1101101 1110000 1100111 100010 111010 100000 110010 110001 101100 100000 100010 1100011 1111001 1101100 100010 111010 100000 110110 101100 100000 100010 1100100 1101001 1110011 1110000 100010 111010 100000 110001 110110 110000 101100 100000 100010 1101000 1110000 100010 111010 100000 110001 110001 110000 1111101 101100 100000 100010 1000100 1100001 1110100 1110011 1110101 1101110 100000 110111 110001 110000 100010 111010 100000 1111011 100010 1101101 1110000 1100111 100010 111010 100000 110010 110010 101110 111000 101100 100000 100010 1100011 1111001 1101100 100010 111010 100000 110100 101100 100000 100010 1100100 1101001 1110011 1110000 100010 111010 100000 110001 110000 111000 101100 100000 100010 1101000 1110000 100010 111010 100000 111001 110011 1111101 101100 100000 100010 1001000 1101111 1110010 1101110 1100101 1110100 100000 110100 100000 1000100 1110010 1101001 1110110 1100101 100010 111010 100000 1111011 100010 1101101 1110000 1100111 100010 111010 100000 110010 110001 101110 110100 101100 100000 100010 1100011 1111001 1101100 100010 111010 100000 110110 101100 100000 100010 1100100 1101001 1110011 1110000 100010 111010 100000 110010 110101 111000 101100 100000 100010 1101000 1110000 100010 111010 100000 110001 110001 110000 1111101 1111101')

socket_address = ("127.0.0.1", 5050)

class test_server(unittest.TestCase):
    def setUp(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("127.0.0.1", 5050))
        self.server.listen(1)

    def tearDown(self):
        self.server.close()
    
if __name__ == '__main__':
    unittest.main()
    