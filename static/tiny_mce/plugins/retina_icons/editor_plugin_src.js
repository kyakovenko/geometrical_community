/**
 * Created with PyCharm.
 * User: Kirill S. Yakovenko
 * E-mail: kirill.yakovenko@gmail.com
 */

(function(tinymce) {
    tinymce.create('tinymce.plugins.RetinaIconsPlugin', {
        init : function(ed, url) {
            // Register commands
            ed.addCommand('mceRetinaIcons', function() {
                ed.windowManager.open({
                    file : url + '/retina_icons.html',
                    width : 360 + parseInt(ed.getLang('retina_icons.delta_width', 0)),
                    height : 460 + parseInt(ed.getLang('retina_icons.delta_height', 0)),
                    inline : 1
                }, {
                    plugin_url : url
                });
            });

            // Register buttons
            ed.addButton('retina_icons', {title : 'Icons', cmd : 'mceRetinaIcons', "class": 'mce_image'});
        },

        getInfo : function() {
            return {
                longname : 'Retina icons',
                author : 'Kirill S. Yakovenko',
                authoremail : 'kirill.yakovenko@gmail.com',
                theme_by: 'http://themeforest.net/user/elemis',
                version : tinymce.majorVersion + "." + tinymce.minorVersion
            };
        }
    });

    // Register plugin
    tinymce.PluginManager.add('retina_icons', tinymce.plugins.RetinaIconsPlugin);
})(tinymce);