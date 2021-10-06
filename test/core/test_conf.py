from app.core.conf import Config


class TestConfig:
    def test_app_config(self):
        conf = Config()
        assert conf.token
