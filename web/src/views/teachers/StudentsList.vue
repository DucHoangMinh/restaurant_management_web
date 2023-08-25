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
                    <v-textarea v-model="student.address" density="compact" rows="2" auto-grow variant="outlined"></v-textarea>
                </v-container>
                </v-card-text>
                <v-card-actions class="delCardAction">
                    <v-btn class="confirmDelButton" @click="adddialog = false">Cancel</v-btn>
                    <v-btn class="" @click="handleAddStudent">Add</v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>
        </v-row>
        <!-- Delete student dialog -->
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
                        <th class="text-left">Name</th>
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
                            <td class="text-left">{{ item.fullname }}</td>
                            <td>{{ item.sex }}</td>
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
    <SnackBar ref="snackbar" v-model:showSnackbar="snackbar.showSnackbar" :message="snackbar.message" />
</template>
<script>
    import {ref , onMounted} from 'vue'
    import axios from 'axios'
    // eslint-disable-next-line no-unused-vars
    import SnackBar from '@/views/components/SnackBar.vue'
    export default {
        setup() {
            const adddialog = ref(false)
            const snackbar = ref({
                showSnackbar: false,
                message: 'Đây là Hoàng Minh Đức',
            });
            const studentsList= ref([])
            async function getStudentList(){
                try {
                    let query = await axios.get('http://127.0.0.1:5000/students')
                    console.log(query.data)
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
                    sex: '',
                    phone: 0,
                    address: '',
            })
            async function handleAddStudent(){
                try{
                    console.log(student.value)
                    await axios.post('http://127.0.0.1:5000/students',student.value)
                    showMessage()
                    adddialog.value = false
                }
                catch(err){
                    console.log('Error: ', err)
                }
            }

            onMounted(() => {
                setUpData();
            })

            function showMessage() {
                snackbar.value.message = 'Đây là thông báo từ snackbar.';
                snackbar.value.showSnackbar = true;
            }
            return {
                adddialog,
                studentsList, 
                student, 
                handleAddStudent, 
                showMessage,
                snackbar
            };
        },  
    }
</script>
<style>
    /* .v-field {
        padding: 4px 0px !important;
    } */
</style>