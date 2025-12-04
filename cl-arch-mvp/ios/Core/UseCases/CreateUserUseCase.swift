// Dominio: Use Case
struct CreateUserRequest {
    let name: String
    let email: String
}

struct CreateUserResponse {
    let userId: String
}

protocol CreateUserUseCase {
    func execute(request: CreateUserRequest) throws -> CreateUserResponse
}

final class CreateUserUseCaseImpl: CreateUserUseCase {
    private let interactor: CreateUserInteractor
    init(interactor: CreateUserInteractor) {
        self.interactor = interactor
    }
    func execute(request: CreateUserRequest) throws -> CreateUserResponse {
        return try interactor.execute(request: request)
    }
}

// Interactor
class CreateUserInteractor {
    func execute(request: CreateUserRequest) throws -> CreateUserResponse {
        // lógica dummy
        return CreateUserResponse(userId: "123")
    }
}

// Coordinator
class CreateUserCoordinator {
    static func build() -> CreateUserUseCase {
        let interactor = CreateUserInteractor()
        return CreateUserUseCaseImpl(interactor: interactor)
    }
}
