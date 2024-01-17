from locust import HttpUser, task, between


class ExchangeRatesAppUser(HttpUser):
    """ Класс для запуска locust задач """
    wait_time = between(0, 0)

    @task
    def courses(self):
        self.client.get('/api/v1/courses/')
