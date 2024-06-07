from user.dao import UserRegisterDAO


class UserServices:

    @staticmethod
    def get_user_exist(user: UserRegisterDAO):
        use=db.query(User).filter_by(User.email ==  user.email)


    