import maya.cmds as cmds
import maya.mel as mel
import json
from maya.plugin.timeSliderBookmark.timeSliderBookmark import getAllBookmarks


def DumpBoommarksJSON():
	
    bookmarks = getAllBookmarks()
    bookmark_names = []
    bookmark_frames = []
    bookmark_data = {}
    
    for i in bookmarks:
        bookmark_names.append(cmds.getAttr(str(i)+".name"))
    for i in bookmarks:
        bookmark_frames.append([cmds.getAttr(str(i)+".timeRangeStart"), cmds.getAttr(str(i)+".timeRangeStop")])
        
    scenename = cmds.file(q=True, sn=True, shn=True)
    scenepath = cmds.file(q=True, sn=True).replace(scenename, '')

    for i, bookmark_name in enumerate(bookmark_names):
        bookmark_data[bookmark_name] = bookmark_frames[i]
    
    with open(str(scenepath)+"BookmarkExport.json", 'wb') as outfile:
        json.dump(bookmark_data, outfile)
    
    cmds.confirmDialog(title="Success!", message="Exported Bookmarks into .json! (Scene folder)", icon="information")
    os.startfile(str(scenepath))

DumpBoommarksJSON()	