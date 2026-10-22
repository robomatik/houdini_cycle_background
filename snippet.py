import hou
import toolutils
 
desktop = hou.ui.curDesktop()
scene_viewers = [
    tab for tab in desktop.paneTabs()
    if isinstance(tab, hou.SceneViewer)
]
 
for sv in scene_viewers:
    viewports = sv.viewports()
     
    for v in viewports:
         
        settings = v.settings()
        cur_scheme = settings.colorScheme()
         
        if cur_scheme == hou.viewportColorScheme.Light:
            settings.setColorScheme(hou.viewportColorScheme.Grey)
            'print ("Color Sheme is changed to Dark")'
        elif cur_scheme == hou.viewportColorScheme.Grey:
            settings.setColorScheme(hou.viewportColorScheme.Dark)
            'print ("Color Sheme is changed to Light")'
        elif cur_scheme == hou.viewportColorScheme.Dark:
            settings.setColorScheme(hou.viewportColorScheme.Light)
            'print ("Color Sheme is changed to Light")'
        else:
            settings.setColorScheme(hou.viewportColorScheme.Dark)
            'print ("Color Sheme is changed to Dark")'
