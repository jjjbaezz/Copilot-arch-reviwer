import XCTest

class CreateUserUseCaseTests: XCTestCase {
    func testExecuteReturnsUserId() throws {
        let useCase = CreateUserCoordinator.build()
        let request = CreateUserRequest(name: "Test", email: "test@email.com")
        let response = try useCase.execute(request: request)
        XCTAssertEqual(response.userId, "123")
    }
}
