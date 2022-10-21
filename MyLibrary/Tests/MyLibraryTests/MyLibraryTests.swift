import XCTest
@testable import MyLibrary

final class MyLibraryTests: XCTestCase {
    public func testLookupTable() throws  {
        
        
        // When
        let lookuptable = try MyLibrary.loadDictionaryFromDisk()
        let answer = lookuptable["fe5dbbcea5ce7e2988b8c69bcfdfde8904aabc1f"]
        
        print(answer)
        
        //Then
        XCTAssertEqual(answer, "8")
    }
    
}
