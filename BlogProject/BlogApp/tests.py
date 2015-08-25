from BlogApp.views import index, blogs, categories, add_blog, create_user, \
    get_date, get_user_by_name, get_blog_and_comment, get_category
from django.test import TestCase, Client
from BlogApp.models import Comment, UserProfile, Blog
from django.utils import timezone
from BlogApp.forms import CommentForm, UserForm, BlogForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from selenium import webdriver
from django.test import LiveServerTestCase


class TestBlogApp(TestCase, LiveServerTestCase):
    fixtures = ['initial_data.json']

    """
    Creating mock user object.
    """

    @classmethod
    def setUp(cls):
        cls.user = User.objects._create_user(username="test_user",
                                             email="test@gmail.com",
                                             password="123", is_staff=True,
                                             is_superuser=False)

        User.objects.create_superuser(username="admin",
                                      email="admin@gmail.com",
                                      password="123")

    """
    Testing all url links which address views and get requests. Testing
    passing variables.
    """

    def test_main_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('all_blogs' in response.context)
        self.assertTrue('login' in response.context)

    def test_blogs_page(self):
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('all_blogs' in response.context)

    def test_categories_page(self):
        response = self.client.get('/Categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('all_categories' in response.context)

    def test_settings_page(self):
        response = self.client.get('/settings/')
        self.assertEqual(response.status_code, 200)

    def test_add_blog_page(self):
        response = self.client.get('/add_blog/')
        self.assertEqual(response.status_code, 200)
        # self.assertTrue('form' in response.context)
        # self.assertTrue('owner' in response.context)

    def test_logout_page(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        response = self.client.get('/create_user/')
        self.assertEqual(response.status_code, 200)

    def test_user_page(self):
        response = self.client.get('/user/onur-hunce/')
        self.assertEqual(response.status_code, 200)
        # self.assertTrue('name' in response.context)
        # self.assertTrue('username' in response.context)

    def test_blog_page(self):
        response = self.client.get('/blog/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['selected_blog'].pk, 1)
        self.assertTrue('Canon' in response.context['selected_blog'].title)
        # checking that non-exist blog throw a 404
        non_exist_response = self.client.get('/blog/35/35/')
        self.assertEqual(non_exist_response.status_code, 404)

    def test_blog_date_page(self):
        response = self.client.get('/2015/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('dates' in response.context)

    def test_get_category_page(self):
        response = self.client.get('/Category/Photography/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('category_type' in response.context)

    def test_dump_page(self):
        response = self.client.get('/wrong/input')
        self.assertEqual(response.status_code, 404)

    """
    End of the testing url links.
    """

    """
    Testing POST requests in views.
    """

    def test_comment_post_in_blog(self):
        response = self.client.post("/blog/11", {"comment_text": 'This is a '
                                                                 'test '
                                                                 'comment.'})
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['Location'], "http://testserver/blog/11/")

    def test_create_user_post(self):
        response = self.client.post("/create_user/", {
            "user": self.user.username, "full_name": "Onur Hunce", "location":
                "Adana", "age": 26
        }, follow=True)

        self.assertEqual(response.status_code, 301)

    """
    Post requests with user profile do not return 301 as I expected. It
    returns 200.
    """
    # def test_adding_new_blog_post(self):
    #     user = UserProfile.objects.get(full_name="Onur Hunce")
    #     response = self.client.post("/add_blog/", {
    #         "title": "deneme", "body": "text", "owner": user
    #     })
    #     # self.assertRedirects(response, '/blogs', status_code=200,
    #     #                      target_status_code=301)
    #     self.assertEqual(response['Location', "http://testserver/add_blog/"])
    """
    End of Testing POST and GET requests in views.
    """

    """
    Testing Forms
    """
    def test_adding_comment_form(self):
        comment_form_data = {"comment_text": 'This is a test comment.',
                             "comment_blog": 1, "comment_name": 1,
                             "comment_mail": "onur@gmail.com"
                             }
        comment_form = CommentForm(data=comment_form_data)
        self.assertTrue(comment_form.is_valid())

    """
    Post requests with user profile do not return 301 as I expected. It
    returns 200.
    """

    # def test_creating_new_user_form(self):
    #     new_user = self.create_test_user()
    #     user_profile = UserProfile.objects.create(user=new_user,
    #                                               full_name="New User",
    #                                               age=45,
    #                                               location="Bandirma")
    #     user_form_data = {"user": user_profile.user, "full_name":
    #                       user_profile.full_name,
    #                       "location": user_profile.location, "age":
    #                           user_profile.age,
    #                       "slug_name": user_profile.slug_name}
    #     user_form = UserForm(data=user_form_data)
    #     print user_form.errors
    #     self.assertTrue(user_form.is_valid())

    #
    # def test_creating_new_blog_form(self):
    #     user = User.objects.create_user(username="unittest")
    #     user_profile= UserProfile.objects.create(user=user, full_name="Onur "
    #                                              "Hunce", location="Ankara",
    #                                              age=25)
    #     blog_form_data = {"title": "test_title", "body": "text", "category":
    #                       "Photography", "owner": user_profile}
    #     blog_form = BlogForm(data=blog_form_data)
    #     print blog_form.non_field_errors
    #     self.assertTrue(blog_form.is_valid())
    """
    End of Testing Forms.
    """

    """
    Testing Models.
    """

    def test_slugify_works_for_user_profile_model(self):
        new_user = self.user
        new_user_profile = UserProfile.objects.create(user=new_user,
                                                      full_name="New User",
                                                      age=45,
                                                      location="Bandirma")
        self.assertEqual("new-user", new_user_profile.slug_name)

    """
    End of Testing Models.
    """

    """
    Testing View Functions
    """

    def test_blogs_view(self):
        response = self.client.get('/blogs/')
        request = blogs(response)
        self.assertEqual(request.status_code, 200)

    def test_categories_view(self):
        response = self.client.get('/Categories/')
        request = categories(response)
        self.assertEqual(request.status_code, 200)

    def test_add_blog_view(self):
        response = self.client.get('/add_blog/')
        self.assertEqual(type(response), HttpResponse)
        test_blog = Blog.objects.get(id=1)
        time_now = timezone.now()
        self.assertTrue(test_blog.publish_date < time_now)
        # response = add_blog(request)
        # self.assertEqual(response.status_code, 200)

    def test_create_user_view(self):
        response = self.client.get('/create_user/')
        self.assertEqual(type(response), HttpResponse)

    def test_get_date_view(self):
        response = self.client.get('/2015/1/')
        request = get_date(response, 1)
        self.assertEqual(request.status_code, 200)

    def test_get_user_by_name_view(self):
        response = self.client.get('/user/onur-hunce/')
        self.assertEqual(type(response), HttpResponse)

    def test_get_blog_and_comment_view(self):
        response = self.client.get('/blog/11/')
        self.assertEqual(type(response), HttpResponse)

    def test_get_category_view(self):
        response = self.client.get('/Category/Fashion')
        request = get_category(response, "Fashion")
        self.assertEqual(request.status_code, 200)

    """
    End of Testing View Functions
    """

    """
    Adding Selenium Tests
    """

    def test_authorized_pages(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.implicitly_wait(30)
        self.selenium.get("%s%s" % (self.live_server_url, "/add_blog"))
        self.selenium.implicitly_wait(100)
        self.selenium.get("%s%s" % (self.live_server_url, "/create_user"))
        self.selenium.implicitly_wait(100)
        self.selenium.get("%s%s" % (self.live_server_url, "/user/onur-hunce/"))
        self.selenium.implicitly_wait(10)

    def test_login_user(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get("%s%s" % (self.live_server_url, "/"))
        username = self.selenium.find_element_by_id("userlogin")
        username.send_keys("onurhunce")
        password = self.selenium.find_element_by_id("password_login")
        password.send_keys("3410")
        self.selenium.find_element_by_xpath(
            '//button[@value="login_button"]').click()
        self.selenium.implicitly_wait(10)
        self.selenium.get("%s%s" % (self.live_server_url,
                                    "/user/onur-hunce/"))

    def test_adding_comment(self):
        self.selenium = webdriver.Firefox()
        self.selenium.maximize_window()
        self.selenium.get("%s%s" % (self.live_server_url, "/blog/1/"))
        self.selenium.implicitly_wait(30)
        username = self.selenium.find_element_by_id("id_comment_name")
        username.send_keys("Selenium Comment")
        email = self.selenium.find_element_by_id("id_comment_mail")
        email.send_keys("selenium@gmail.com")
        comment = self.selenium.find_element_by_id("id_comment_text")
        comment.send_keys("This is a selenium comment!")
        self.selenium.implicitly_wait(10)
        self.selenium.find_element_by_xpath(
            '//button[@value="Submit"]').click()

        """
        End of Selenium Tests
        """