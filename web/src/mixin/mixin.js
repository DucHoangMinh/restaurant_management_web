export const mixin = {
    data(){

    },
    methods:{
        getCookieValue: function(name) {
            return document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
        }
    }
}