#!/usr/bin/env python
# coding: utf-8

# In[31]:


import tarfile
import numpy as np
import time
from PIL import Image
from io import BytesIO


# In[33]:


class loadDtar(object):
    def __init__(self, path):
        '''
        description : init all parameters
        path : accept relative/absolute path
        '''
        self.path = path

    def getHeader(self):
        '''
        description : get all files in tar_ball
        '''
        try:
            s = time.time();
            t_b = tarfile.open(self.path);
            t_b_a = t_b.getnames();
            e = time.time();
            print('spend {} secs loading tarfile'.format(e-s))
            return t_b_a
        except Exception as e:
            print(e)
            
    def getOneExtract(self,selected,mode=None):
        '''
        description : get only selected image in numpy array format
        selected : string i.e. 'all_souls_000000.jpg'
        format : if mode == 'text', select decode format default = utf-8
        '''
        try :
            t_b = tarfile.open(self.path); 
            ext = t_b.extractfile(selected)
            b_ext = ext.read();
            if mode == 'image': 
                img = np.array(Image.open(BytesIO(b_ext)));
                return img
            elif mode == 'text':
                txt = b_ext.decode("utf-8")
                return txt
            elif mode == 'byte':
                return b_ext  
            elif mode == None:
                print('Please select decode mode i.e. "image","text" ')
        except Exception as e :
            print(e)

