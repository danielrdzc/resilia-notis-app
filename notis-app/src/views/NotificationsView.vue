<template>
    <v-container fluid>
        <h1 class="text-center">Notifications</h1>
        <v-list class="mt-4 pa-4">
            <v-list-item class="mb-4" v-for="noti in notifications"
            :prepend-avatar="avatar"
            :title="noti.title"
            :subtitle="noti.content">
            </v-list-item>
        </v-list>
    </v-container>
</template>

<script>
import UserNotificationService from '@/services/UserNotificationService'
export default {
    data: () => ({
        userData: JSON.parse(localStorage.getItem('userData')),
        notifications: [],
        avatar: ''
    }),
    async mounted() {
        this.notifications = await UserNotificationService.getAllNotis(this.userData.id);
        if (this.userData.role == 1) {
            this.avatar = 'https://cdn.vuetifyjs.com/images/lists/5.jpg';
        } else {
            this.avatar = 'https://cdn.vuetifyjs.com/images/john.png'
        }
    }
}
</script>