// Dominio: Use Case
data class CreateUserRequest(
    val name: String,
    val email: String
)

data class CreateUserResponse(
    val userId: String
)

interface CreateUserUseCase {
    fun execute(request: CreateUserRequest): CreateUserResponse
}

class CreateUserUseCaseImpl(private val interactor: CreateUserInteractor) : CreateUserUseCase {
    override fun execute(request: CreateUserRequest): CreateUserResponse {
        return interactor.execute(request)
    }
}

// Interactor
class CreateUserInteractor {
    fun execute(request: CreateUserRequest): CreateUserResponse {
        // lógica dummy
        return CreateUserResponse(userId = "123")
    }
}

// Coordinator
object CreateUserCoordinator {
    fun build(): CreateUserUseCase {
        val interactor = CreateUserInteractor()
        return CreateUserUseCaseImpl(interactor)
    }
}
