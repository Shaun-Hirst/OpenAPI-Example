# pylint: disable=E0401, R0903
# E0401: has been disabled as imports aren't found until build time
# R0903: Too few public methods
"""
api server database connection config

creator: shaun.hirst@3adesign.co.uk
created: 26/02/2020
"""

from decouple import config


class Config():
    """ base configuration"""
    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='04d3a022-c346-49c0-9c03-e9df93b335fa')


class ProductionConfig(Config):
    """production configuration"""
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600


class DebugConfig(Config):
    """Debug configuration"""
    DEBUG = True


# Load all possible configurations
CONFIG_DICT = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
