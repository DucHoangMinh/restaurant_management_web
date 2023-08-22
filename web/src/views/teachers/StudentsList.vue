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
                        <th class="text-center">Email</th>
                        <th class="text-center">Sex</th>
                        <th class="text-center">Phone</th>
                        <th class="text-center">Address</th>
                    </tr>
                    </thead>
                    <tbody>
                        <!-- <tr
                            v-for="item in studentsList"
                            :key="item.id"
                        >
                            <td>{{ item.name }}</td>
                            <td>{{ item.calories }}</td>
                        </tr> -->
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
            const studentsList= ref([])

            async function getStudentList(){
                try {
                    let query = await axios.get('http://127.0.0.1:5000/students')
                    return query.data
                } catch (error) {
                    console.log(error)
                }
            }
            async function setUpData(){
                studentsList.value = await getStudentList()
            }
            onMounted(() => {
                setUpData();
            });
            return {
                studentsList,
            };
        },  
    }
</script>
<style>
    .v-field {
        padding: 4px 0px !important;
    }
</style>