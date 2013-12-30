'''
Created on Dec 18, 2013

@author: pandazen
'''
'''
Created on Dec 10, 2013

@author: pandazen
'''
import os
import logging
import logconfig
import subprocess
import mapdrive
import filecmpnoext

conn_log = logging.getLogger('mis_compare')
### begin prepare path
drive1 = 'P:\\'
drive2 = 'Q:\\'

#===========================================================================
# path1 = '\\\\192.168.51.233\\c$\\fmb'
# path2 = '\\\\192.168.51.233\\c$\\fmx'
# user1 = 'administrator'
# user2 = 'administrator'
# pw1 = 'wi'
# pw2 = 'wi'
#===========================================================================

path1 = '\\\\192.168.51.10\\fmbs$'
path2 = '\\\\192.168.51.2\\mis3.5$\\FORMS'
user1 = 'administrator'
user2 = 'administrator'
pw1 = 'ADMIN.10..'
pw2 = 'admin.02'


mapdrive.netUse(drive1, path1, user1, pw1)
mapdrive.netUse(drive2, path2, user2, pw2)
### end prepare path


def db_fmb():
    d = 'to be db'
    print(d)
    
def fmb_fmx():    
    if os.path.exists(drive1) and os.path.exists(drive2):
        
        conn_log.info('open textfile to print ' + os.getcwd() + '\\' + logconfig.logFile)        
        
        comparison = filecmpnoext.dircmp(drive1, drive2, ['BACK','Back','back','backup','!backup'],[],'diffext')
        comparison.report_diffonly_closure()
        
        conn_log.info('Done, save log to ' + os.getcwd() + '\\' + logconfig.logFile)
        
        
        if os.path.isfile(os.getcwd() + '\\' + logconfig.logFile):
            try:
                os.startfile(logconfig.logFile)
            except AttributeError:
                subprocess.call(['open', logconfig.logFile])
    else:
        conn_log.warning('drive ' + drive1 + ' dan/atau ' + drive2 + ' tidak ditemukan!')

if __name__ == '__main__':         
    fmb_fmx()
    
    
    