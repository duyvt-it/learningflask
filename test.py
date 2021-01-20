from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='abc')
        u.set_password('abc')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('abc'))

    # def test_avatar(self):
    #     u = User(username='abc', email='duy@duy.com')
    #     self.assertEqual(
    #         u.avatar(128),
    #         'https://www.gravatar.com/avatar/'
    #         'd4c74594d841139328695756648b6bd6'
    #         '?d=identicon&s=128'
    #     )

    def test_follow(self):
        u1 = User(username='duy', email='duy@duy.com')
        u2 = User(username='duyvt', email='duyvt@duyvt.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'duyvt')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'duy')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # Create 4 Users
        u1 = User(username = 'duy', email = 'duy@duy.com')
        u2 = User(username = 'tram', email = 'tram@tram.com')
        u3 = User(username = 'na', email = 'na@na.com')
        u4 = User(username = 'thao', email = 'thao@thao.com')
        db.session.add_all([u1, u2, u3, u4])
        db.session.commit()

        # Create 4 posts for check
        now = datetime.utcnow()
        p1 = Post(body="post cua Duy", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post cua Tram", author=u2, timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post cua Na", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post cua Thao", author=u4, timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # Config followers
        u1.follow(u2) # Duy follow Tram
        u1.follow(u3) # Duy follow Chi Na
        u2.follow(u4) # Tram follow Thao
        u3.follow(u4) # Chi Na follow Thao
        db.session.commit()

        # Check all Post have been followed by User
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p3, p1])
        self.assertEqual(f2, [p2, p4])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)