<template>
    <v-row>
      <v-col cols="12" sm="12" class="pa-12">
        <v-row align="center" justify="center">
          <v-col class="admin-text" cols="12" sm="12">
            <h2 class="text-center">
              <v-icon color="white">mdi-account-circle</v-icon>
              WRAP
            </h2>
          </v-col>
          <v-col cols="6" sm="12" md="8">
            <v-card class="elevation-12">
              <!-- LOGIN CARD TOOLBAR -->
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title>
                  <v-icon>mdi-login</v-icon>
                  Log In
                </v-toolbar-title>
                <v-spacer/>
              </v-toolbar>
              <!-- LOGIN CARD TOOLBAR -->
  
              <!-- LOGIN INPUT FORM -->
              <v-card-text>
                <v-form>
                  <v-text-field outlined v-model="username" label="Username"
                                color="secondary"
                                name="login" prepend-icon="mdi-account" type="text"/>
  
                  <v-text-field outlined v-model="password" id="password"
                                label="Password" color="secondary"
                                name="password" prepend-icon="mdi-lock" type="password"
                                @keypress.enter="authUser"/>
                </v-form>
              </v-card-text>
              <!-- LOGIN INPUT FORM -->
  
              <!-- LOGIN BUTTONS -->
              <v-card-actions>
                <v-spacer/>
                <v-btn @click="authUser()" color="secondary">Enter</v-btn>
              </v-card-actions>
              <!-- LOGIN BUTTONS -->
  
            </v-card>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
</template>
  
<script>
import LoginService from '@/services/LoginService';

export default {
name: 'login-card',
props: {
    source: String,
},
data: () => ({
    username: '',
    password: '',
}),
methods: {
    async authUser() {
        const token = await this.$messaging.getToken({ vapidKey: 'BFQh2ZqRnGeFmHzlN95-oMTHrpdJBDPvy0jn86QFjoFaMNf-e9vQz1L56Uwm1325OJTf5eKsMfENzESHnMr7J3g' });
        const resp = await LoginService.login(this.username, this.password, token);
        localStorage.setItem('userData', JSON.stringify(resp));
        this.$router.push('/dashboard');
    },
},
};
</script>


<style>
.admin-text {
z-index: 1;
}

h2 {
letter-spacing: 0.25rem;
color: white;
font-size: 2rem;
font-weight: 300;
}
</style>
