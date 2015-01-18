import sys

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout

from flatui.flatui import FlatButton, FloatingAction

Builder.load_file( 'test.kv' )


class Test( BoxLayout ) :
    
    def __init__( self, **kargs ) :
        super( Test, self ).__init__( **kargs )


class TestApp( App ) :
    
    def build( self ) :
        self.t = Test()
        return self.t

if __name__ == '__main__':
    TestApp().run()



