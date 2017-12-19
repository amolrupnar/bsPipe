import pymysql

from bsPipe.bs_core import bs_pathGenerator

reload(bs_pathGenerator)


class Bs_Database(object):
    def __init__(self):
        self.host = '192.168.0.220'
        self.user = bs_pathGenerator.bs_getEnv()['projectShort']
        # self.user = 'kns'
        self.password = '1234'
        self.database = bs_pathGenerator.bs_getEnv()['projectName']
        # self.database = 'kicko_speedo'
        self.dtConn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database)
        self.dtCur = self.dtConn.cursor()

    def __exit__(self, *_):
        self.dtCur.close()

    def bs_databaseAssetPublish(self, tableName, fileName, fileOwner, fileSize, dateTime, comment):
        # create table if not exist.
        createTable = 'CREATE TABLE IF NOT EXISTS `{database}`.`{table}` ( `fileName` VARCHAR(50) NOT NULL , ' \
                      '`fileOwner` VARCHAR(50) NOT NULL , `fileSize` VARCHAR(50) NOT NULL , ' \
                      '`dateTime` VARCHAR(50) NOT NULL , `comment` TEXT, PRIMARY KEY (`fileName`)) ENGINE = MyISAM;' \
            .format(database=self.database, table=tableName)
        self.dtCur.execute(createTable)
        # insert data into table.
        dataForTable = "REPLACE INTO `{table}` (`fileName`, `fileOwner`, `fileSize`, `dateTime`, `comment`) VALUES " \
                       "({fileName}, {fileOwner}, {fileSize}, {dateTime}, {comment});".format(
                                                                                    table=tableName,
                                                                                    fileName=repr(fileName),
                                                                                    fileOwner=repr(fileOwner),
                                                                                    fileSize=repr(fileSize),
                                                                                    dateTime=repr(dateTime),
                                                                                    comment=repr(comment))
        self.dtCur.execute(dataForTable)

    def bs_databaseAssetComment(self, tableName, fileName):
        getComment = 'SELECT comment FROM {tableName} WHERE fileName={fileName};'.format(tableName=tableName,
                                                                                         fileName=repr(fileName))
        self.dtCur.execute(getComment)
        return str(self.dtCur.fetchone()[0])
