import org.junit.Assert.assertEquals
import org.junit.Test

class CreateUserUseCaseTest {
    @Test
    fun testExecuteReturnsUserId() {
        val useCase = CreateUserCoordinator.build()
        val request = CreateUserRequest(name = "Test", email = "test@email.com")
        val response = useCase.execute(request)
        assertEquals("123", response.userId)
    }
}
