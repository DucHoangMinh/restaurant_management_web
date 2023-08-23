<template>
    <v-container>
        <div id="heading">
            <div class="heading__wrapper d-flex align-center justify-space-between" 
                style="border-bottom: 1px solid #ccc;padding: 12px;margin:12px">
                <div class="heading__title">
                    <v-chip class="p-4 text-body-1" variant="outlined" style="">
                        <font-awesome-icon class="text-body-1" icon="fa-solid fa-user" style="margin-right: 8px;"/>
                        Students List
                    </v-chip>
                </div>
                <div class="schoolName d-flex align-center">
                    <v-chip class="text-body-1" variant="text">
                        Hanoi High School
                        <font-awesome-icon class="text-h5" style="margin-left: 8px;" color="primary" icon="fa-solid fa-school" />
                    </v-chip>
                </div>
            </div>
            <div class="heading__filter d-flex justify-space-between align-center">
                <div class="">
                    <v-text-field label="Tìm kiếm theo tên" variant="outlined" style="min-width: 200px;"></v-text-field>
                </div>
                <div class="createNewStudent">
                    <v-btn color="#3bd16f" style="color: #fff;">
                        New student
                        <font-awesome-icon style="margin-left: 8px;" class="" icon="fa-solid fa-user-plus"/>
                    </v-btn>
                </div>
            </div>
        </div>
        <div id="body">
            <div class="body__wrapper">
                <v-table density="compact">
                    <thead>
                    <tr>
                        <th class="text-center">Name</th>
                        <th class="text-center">Sex</th>
                        <th class="text-center">Email</th>
                        <th class="text-center">Phone</th>
                        <th class="text-center">Address</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="(item,index) in studentsList"
                            :key="index"
                            style="padding: 4px;"
                        >
                            <td>{{ item.name }}</td>
                            <td>{{ item.sex ? 'Nam' : 'Nữ' }}</td>
                            <td>{{ item.email }}</td>
                            <td>{{ item.phone }}</td>
                            <td>{{ item.address }}</td>
                            <td class="d-flex justify-center align-center">
                                <div class="editButton rounded-circle" style="padding: 6px;background-color: #3bd16f;" >
                                    <font-awesome-icon icon="fa-solid fa-pen" color="#fff" style="cursor: pointer;"/>
                                </div>
                                <div class="deleteButton ml-4 rounded-circle" style="padding: 6px;background-color:  #f32013;">
                                    <font-awesome-icon icon="fa-solid fa-trash" color="#fff" style="cursor: pointer;"/>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </v-table>
            </div>
        </div>
    </v-container>
</template>
<script>
    import {ref , onMounted} from 'vue'
    import axios from 'axios'
    export default {
        setup() {
            const studentsList= ref([{
                name: 'Hoàng Minh Đức',
                sex: true,
                email:'hoangminhduc4125@gmail.com',
                phone: '0869870245',
                address:'Hà Trung, Thanh Hóa'
            },{
                name: 'Hoàng Minh Khánh',
                sex: true,
                email:'hoangminhkhanh4125@gmail.com',
                phone: '0869870249',
                address:'Hà Trung, Thanh Hóa'
            }])

            async function getStudentList(){
                try {
                    let query = await axios.get('http://127.0.0.1:5000/students')
                    return query.data
                } catch (error) {
                    console.log(error)
                }
            }
            // eslint-disable-next-line no-unused-vars
            async function setUpData(){
                studentsList.value = await getStudentList()
            }
            onMounted(() => {
                // setUpData();
            });
            return {
                studentsList,
            };
        },  
    }
</script>
<style>
    /* .v-field {
        padding: 4px 0px !important;
    } */
</style>