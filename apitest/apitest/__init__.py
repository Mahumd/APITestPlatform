import pymysql

# 解决数据库版本问题引起的影响
pymysql.version_info = (1,4,13,"final",0)
# 解决数据库连接问题
pymysql.install_as_MySQLdb()