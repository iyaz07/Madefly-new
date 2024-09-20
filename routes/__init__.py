from routes.about import about_bp
from routes.admin import admin_bp
from routes.comefly import comefly_bp
from routes.register import fly_status_bp
from routes.gofly import gofly_bp
from routes.home import home_bp
from routes.admin_login import admin_login_bp
from routes.admin_dashboard import admin_dashboard_bp
from routes.meal_plan import meal_plan_bp
from routes.activity_plan import activity_plan_bp


def register_routes(app):
    app.register_blueprint(about_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(comefly_bp)
    app.register_blueprint(fly_status_bp)
    app.register_blueprint(gofly_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(admin_login_bp)
    app.register_blueprint(admin_dashboard_bp)
    app.register_blueprint(meal_plan_bp)
    app.register_blueprint(activity_plan_bp)
