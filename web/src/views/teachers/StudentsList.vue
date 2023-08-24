<template>
    <v-container>
        <!-- Add student dialog -->
        <v-row justify="center">
            <v-dialog
                v-model="adddialog"
                max-width="500"
            >
            <v-card>
                <v-card-title class="addFormTitle">
                    <span>New student</span>
                </v-card-title>
                <v-card-text>
                <v-container>
                    <label class="inputFieldTitle">Name</label>
                    <v-text-field density="compact" variant="outlined" v-model="student.fullname"></v-text-field>
                    <label class="inputFieldTitle">Phone</label>
                    <v-text-field density="compact" variant="outlined" type="number" v-model="student.phone"></v-text-field>
                    <label>Email</label>
                    <v-text-field density="compact" variant="outlined" v-model="student.email" type="email" class="inputEmail"></v-text-field>
                    <label class="inputFieldTitle">Date of birth</label>
                    <v-text-field density="compact" variant="outlined" type="date" v-model="student.dob"></v-text-field>
                    <div class="pb-4 d-flex align-center justify-space-between">
                        <label>Giới tính: {{ sex }}</label>
                        <div class="d-flex align-center justify-space-between">
                            <input type="radio" value="Nam" v-model="student.sex" style="cursor: pointer;">
                                <label>Nam</label>
                            <input class="ml-4" type="radio" v-model="student.sex" value="Nữ" style="cursor: pointer;">
                                <label>Nữ</label>
                        </div>
                    </div>
                    <lable>Address</lable>
                    <v-textarea density="compact" rows="2" auto-grow variant="outlined"></v-textarea>
                </v-container>
                </v-card-text>
                <v-card-actions class="delCardAction">
                    <v-btn class="confirmDelButton" @click="adddialog = false">Cancel</v-btn>
                    <v-btn class="" @click="handleAddStudent">Add</v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>
        </v-row>
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
                    <v-btn color="#3bd16f" style="color: #fff;" @click="adddialog = true">
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
        data() {
            return {
                adddialog: true,
            }
        },
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

            const student = ref({
                    fullname: '',
                    dob: null,
                    email: '',
                    sex: 0,
                    phone: 0,
                    address: '',
            })
            async function handleAddStudent(){
                console.log(student.value)
            }

            onMounted(() => {
                // setUpData();
            });
            return {
                studentsList, student, handleAddStudent
            };
        },  
    }
</script>
<style>
    /* .v-field {
        padding: 4px 0px !important;
    } */
</style>