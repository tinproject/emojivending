import random

from locust import HttpLocust, TaskSet, task


class BuyEmoji(TaskSet):
    @task(100)
    def landing(self):
        self.client.get("/")

    @task(70)
    def request_emoji(self):
        category_id = "cat" + str(random.randint(1, 6))
        data = {
            "category": category_id
        }
        self.client.post("/request-emoji", data=data)

    @task(40)
    def send_feedback(self):
        # simulate a 65% of possitive feedback
        feedback = "yes" if random.random() <= 0.5 else "no"
        data = {
            "feedback": feedback
        }
        self.client.post("/send-feedback", data=data)


class WebsiteUser(HttpLocust):
    task_set = BuyEmoji
    min_wait = 1000
    max_wait = 8000
