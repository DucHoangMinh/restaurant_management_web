export const mixin = {
    data(){

    },
    methods:{
        getCookieValue: function(name) {
            return document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)')?.pop() || ''
        },
        formatToPostgreTimeStamp: function(dateString){
            const dateObj = new Date(dateString);

            const year = dateObj.getFullYear();
            const month = String(dateObj.getMonth() + 1).padStart(2, "0"); // Thêm 0 đằng trước nếu tháng < 10
            const day = String(dateObj.getDate()).padStart(2, "0"); // Thêm 0 đằng trước nếu ngày < 10
            const hours = String(dateObj.getHours()).padStart(2, "0");
            const minutes = String(dateObj.getMinutes()).padStart(2, "0");
            const seconds = String(dateObj.getSeconds()).padStart(2, "0");

            const formattedDate = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
            return formattedDate;
        }

    }
}