<template>
    <v-container>
        <!-- Delete student dialog -->
        <v-row justify="center">
            <v-dialog
                v-model="deldialog"
                max-width="500"
            >
              <v-card>
                <v-card-text>
                  Bạn có chắc chắn muốn xóa sinh viên {{ studentToDel.fullname }}
                </v-card-text>
                <div class="d-flex align-center justify-space-between">
                  <v-btn color="green" @click="deldialog = false">Hủy</v-btn>
                  <v-btn color="warning" @click="handleDelete">Xác nhận xóa</v-btn>
                </div>
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
                    <v-btn color="#3bd16f" style="color: #fff;" @click="toCreatePage">
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
                            <td>{{item.address}}</td>
                            <td class="d-flex justify-center align-center">
                                <div class="editButton rounded-circle" style="padding: 6px;background-color: #3bd16f;" >
                                    <font-awesome-icon icon="fa-solid fa-pen" color="#fff"
                                     @click="() => toEditPage(item)"
                                     style="cursor: pointer;"/>
                                </div>
                                <div class="deleteButton ml-4 rounded-circle"
                                     @click="() => openDelDialog(item)"
                                     style="padding: 6px;background-color:  #f32013;cursor: pointer">
                                    <font-awesome-icon icon="fa-solid fa-trash" color="#fff"/>
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
import {ref, onMounted} from 'vue'
import axios from 'axios'
import {useRouter} from 'vue-router'
export default {
    setup() {
      const deldialog = ref(false)
      const router = useRouter()
      const studentToDel = ref(null)
        const snackbar = ref({
            showSnackbar: false,
            message: 'Đây là Hoàng Minh Đức',
        });
        const studentsList= ref([])
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
            setUpData();
        })

        function showMessage() {
            snackbar.value.message = 'Đây là thông báo từ snackbar.';
            snackbar.value.showSnackbar = true;
        }
        function toCreatePage(){
          router.push('/teachers/student-list/add')
        }
        function toEditPage(email){
          router.push(
            `/teachers/student-list/edit/${email}`,
          )
        }
        function openDelDialog(student){
          studentToDel.value = student;
          deldialog.value = true
        }
        async function handleDelete(){
          await axios.delete(`http://127.0.0.1:5000/students/${studentToDel.value.email}`)
          router.push('/teachers/student-list')
        }
        return {
          snackbar,
          studentsList,
          showMessage,
          toCreatePage,
          toEditPage,
          deldialog,
          openDelDialog,
          studentToDel,
          handleDelete
        }
    },
    }
</script>
<style>
    /* .v-field {
        padding: 4px 0px !important;
    } */
</style>