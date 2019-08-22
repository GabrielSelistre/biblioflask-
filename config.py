#config.py: config para ambientes de prod/teste/dev
class Config():
    # configurações comuns a T0D0S ambientes
    SECRET_KEY='umdoistresquatrocincoseisojoséricardoéumsiamês'

class DevelopmentConfig(Config):
    DEBUG=True

class TestConfig(Config):
    DEBUG=True

class ProductionConfig(Config):
    DEBUG=False

app_config={'development':DevelopmentConfig,
            'test'       :TestConfig,
            'production' :ProductionConfig}
