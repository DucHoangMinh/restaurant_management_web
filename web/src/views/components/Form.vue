<!-- eslint-disable vue/multi-word-component-names -->
<template>
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
</template>
<script>
</script>