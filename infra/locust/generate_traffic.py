import random

from locust import HttpUser, TaskSet, task, between


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
        # simulate a 50% of possitive feedback
        feedback = "yes" if random.random() >= 0.5 else "no"
        data = {
            "feedback": feedback
        }
        self.client.post("/send-feedback", data=data)


class WebsiteUser(HttpUser):
    tasks = [BuyEmoji]
    wait_time = between(1, 8)
