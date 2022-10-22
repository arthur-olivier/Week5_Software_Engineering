# Week5_Software_Engineering

a) 
I build a python file who create a lookup table with all the letters between a-z,A-Z and 0-9 and there hash with sha1. 
This python file create a json file with the lookup table.
I build a swift package which open the data.json create by the python file and which crack a hashcode to find the letter/number which correspond to the
hash we specified.

b) For the python file, you just have to run the python file and it will create automatically the lookuptable.
After, you have to put the data.json file in the folder MyLibrary/Sources/ and in the package swift you have to write the hash you want to crack .
But also the result that you expect in XCTAssertEqual(answer, "your expection")
After you just have to build the package and to run the test .
