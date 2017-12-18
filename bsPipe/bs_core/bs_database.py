import pymysql


from bsPipe.bs_core import bs_pathGenerator

reload(bs_pathGenerator)


class Bs_Database(object):
    def __init__(self):
        self.host = '192.168.0.220'
        # TODO: change it according to environment variable once this script is complete.
        self.user = bs_pathGenerator.bs_getEnv()['projectShort']
        # self.user = 'kns'
        self.password = '1234'
        self.database = bs_pathGenerator.bs_getEnv()['projectName']

    def bs_databaseAssetPublish(self, tableName, fileName, fileOwner, fileSize, dateTime, comment):
        dtConn = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.database)
        dtCur = dtConn.cursor()
        # create table if not exist.
        createTable = 'CREATE TABLE IF NOT EXISTS `{database}`.`{table}` ( `fileName` VARCHAR(50) NOT NULL , ' \
                      '`fileOwner` VARCHAR(50) NOT NULL , `fileSize` VARCHAR(50) NOT NULL , ' \
                      '`dateTime` VARCHAR(50) NOT NULL , `comment` TEXT, PRIMARY KEY (`fileName`)) ENGINE = MyISAM;' \
            .format(database=self.database, table=tableName)
        dtCur.execute(createTable)
        # insert data into table.
        dataForTable = "REPLACE INTO `{table}` (`fileName`, `fileOwner`, `fileSize`, `dateTime`, `comment`) VALUES " \
                       "({fileName}, {fileOwner}, {fileSize}, {dateTime}, {comment});".format(
                        table=tableName,
                        fileName=repr(fileName),
                        fileOwner=repr(fileOwner),
                        fileSize=repr(fileSize),
                        dateTime=repr(dateTime),
                        comment=repr(comment))
        dtCur.execute(dataForTable)

    @staticmethod
    def bs_fetchDatabase():
        print 111111111


if __name__ == '__main__':
    print 111111111
    # a = bs_database('kicko_speedo')
    # a.bs_databaseAssetPublish('kns_ch_kicko_mod', 'kns_ch_kicko_mod_v005', 'amol', '12MB', '12PM', 'verison_5')
    # a.bs_databaseAssetPublish('kns_ch_kicko_mod', 'kns_ch_kicko_mod_v006', 'amol', '12MB', '12PM', 'version_6')
