/**
 * Created with PyCharm.
 * User: Kirill S. Yakovenko
 * E-mail: kirill.yakovenko@gmail.com
 */

tinyMCEPopup.requireLangPack();

var RetinaIcons = {
    init : function(ed) {
        tinyMCEPopup.resizeToInnerSize();
        var uls = document.getElementsByTagName('ul'), parent, i;
        for(i in uls) {
            if (uls[i].className == 'retina-icons'){
                parent = uls[i];
                break;
            }
        }
        var links = parent.getElementsByTagName('a');
        for(i in links) {
            links[i].style.cursor = "pointer";
            links[i].onclick = this.insert;
        }

    },

    insert : function(event) {
        var ed = tinyMCEPopup.editor, dom = ed.dom,
            background = document.getElementById('background');

        tinyMCEPopup.execCommand('mceInsertContent', false, dom.createHTML('i', {
            "class": event.currentTarget.innerText + (background.checked?' awe':'')},
            "&#11;")
        );

        tinyMCEPopup.close();
    }
};

tinyMCEPopup.onInit.add(RetinaIcons.init, RetinaIcons);