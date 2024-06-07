from doamins.user.service import UserServices

class UserServicesGETApp:

    def __init__(requst: Request, dao: UserRegisterDAO):
        
    async def invoke():
        await checkuser_exist() 

    async checkuser_exist() :
        userExist = UserServices.get_user_exist(dao)
        