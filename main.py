import git
import os

work_dir = 'D:\\work\\FORS\\OATI'
fors_username = 'alexander.breev'
fors_password = 'C0mplexIT123'


git.Git(work_dir).clone('https://'+str(fors_username)+':'+str(fors_password)+'@stash.fors.ru/scm/oati/insp_oati.git', branch='oati-insp-7.2.7')