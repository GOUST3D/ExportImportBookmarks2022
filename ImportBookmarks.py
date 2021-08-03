import maya.cmds as cmds
import maya.mel as mel
import json
from maya.plugin.timeSliderBookmark.timeSliderBookmark import getAllBookmarks, updateBookmark, createBookmark


def ImportBoommarksJSON():
	
    bookmarks = getAllBookmarks()
    bookmark_names = []
    bookmark_frames = []
    bookmarks_import = {}
    
    scenename = cmds.file(q=True, sn=True, shn=True)
    scenepath = cmds.file(q=True, sn=True).replace(scenename, '')
    
    with open(str(scenepath)+"BookmarkExport.json") as infile:
        bookmark_data = json.load(infile)
    
    for i in bookmark_data:
        bookmarks_import[i] = bookmark_data[i]

    for i, name in enumerate(bookmarks_import):
        length_start = 0
        if len(bookmarks) == 0:
            print("BOOKMARKS IS 0!")
            createBookmark(name=name, start=bookmarks_import[name][0], stop=bookmarks_import[name][1])
        else:
            for bookmark in bookmarks:
                length = len(bookmarks)
                length_start += 1
                if name == cmds.getAttr(bookmark+".name"):
                    updateBookmark(bookmark, start=bookmarks_import[name][0], stop=bookmarks_import[name][1])
                    break
                if length_start == length:
                    createBookmark(name=name, start=bookmarks_import[name][0], stop=bookmarks_import[name][1])

    cmds.confirmDialog(title="Success!", message="Imported & Bookmarks from BookmarkExport.json! (Scene folder)", icon="information")

ImportBoommarksJSON()
