import os


def add_profile(username, password, email, picture=None, website=None, friends=None):
    def create_user(username, password, email):
        return User.objects.get_or_create(username=username, 
                                          password=password, email=email)[0]
    # def create_profile(user, picture=None, website=None, friends=None):
        # return UserProfile.objects.get_or_create(user=user, picture=picture,
                                                 # website=website, friends=friends)[0]
    def create_profile(user):
        return UserProfile.objects.get_or_create(user=user)[0]
    user = create_user(username=username, password=password, email=email)
    return create_profile(user=user)

def populate():
    # a = add_profile(username='a', password='a', email='a@a.com')
    b = add_profile(username='b', password='b', email='b@b.com')
    # c = add_profile(username='c', password='c', email='c@c.com')
    # d = add_profile(username='d', password='d', email='d@d.com')
    # e = add_profile(username='e', password='e', email='e@e.com')
    # f = add_profile(username='f', password='f', email='f@f.com')
    # g = add_profile(username='g', password='g', email='g@g.com')
    # h = add_profile(username='h', password='h', email='h@h.com')
    # i = add_profile(username='i', password='i', email='i@i.com')

if __name__ == '__main__':
    print('Starting profile population script...')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langtank.settings')
    from django.contrib.auth.models import User
    from tank.models import UserProfile
    populate()
