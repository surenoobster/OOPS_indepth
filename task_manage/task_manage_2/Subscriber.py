class NewsPublisher:
    def __init__(self):
        self._subscribers = []
        self._latest_news = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def add_news(self, news):
        """Adds news and notifies all subscribers."""
        self._latest_news = news
        self.notify_subscribers()
        self.print_news()  # Print news here

    def get_news(self):
        """Returns the latest news."""
        return self._latest_news

    def print_news(self):
        """Prints the latest news (instead of Subscriber doing it)."""
        print(f"News Update: {self._latest_news}")


class Subscriber:
    def update(self):
        """Placeholder method (does nothing)."""
        pass


# **Usage**
publisher = NewsPublisher()

# Creating subscribers
subscriber1 = Subscriber()
subscriber2 = Subscriber()

# Attaching subscribers to publisher
publisher.attach(subscriber1)
publisher.attach(subscriber2)

# Adding news (Publisher will print news)
publisher.add_news("Breaking News: Python 4.0 Released!")
publisher.add_news("Update: Python 4.0 comes with new AI features!")
