<template>
    <v-toolbar title="WRAP" color="primary">
        <v-btn to="/dashboard"
            stacked
            >
            <v-icon icon="mdi-view-dashboard"></v-icon>

            Dashboard
        </v-btn>

        <v-btn @click="goToNotifications()"
        stacked>
            <v-badge v-if="notiReceivedFlag" color="error" dot>
                <v-icon icon="mdi-bell"></v-icon>
            </v-badge>
            <v-icon v-else icon="mdi-bell"></v-icon>
            Notis
        </v-btn>

        <v-btn to="/"
            stacked
            >
            <v-icon icon="mdi-login"></v-icon>

            Logout
        </v-btn>
    </v-toolbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
name: 'app-navbar',
data: () => ({
    notiReceived: false,
}),
computed: {
    ...mapGetters({
      notiReceivedFlag: 'notiReceivedFlag'
    })
},
mounted() {
    this.$messaging.onMessage((payload) => {
            this.notiReceived = true;
    });
},
methods: {
    goToNotifications() {
        this.$store.commit('notiDismissed');
        this.$router.push('/notifications');
    }
}
};
</script>