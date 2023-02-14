<template>
    <v-container fluid class="text-center">
        <h1>Dashboard</h1>
        <v-btn color="success" v-if="userData.role==2" to="create-commission-request"><v-icon icon="mdi-plus"></v-icon>Create Commission Request</v-btn>

        <v-container>
            <v-card class="mt-4">
                <v-card-item>
                    <v-card-title><b>Pending Commission Requests</b></v-card-title>
                </v-card-item>

                <v-card-item>
                    <v-card-text>
                        <v-row>
                            <v-col cols="4" v-for="request in pendingCommissionRequests">
                                <v-card>
                                    <v-card-item>
                                        <v-card-text v-if="userData.role==1">
                                            <b>Company:</b> {{request.requesting_user_id}}
                                            <b>Commission Type:</b> {{request.request_type == 1 ? 'Sculpture' : request.request_type == 2 ? 'Painting' : 'Other'}}
                                        </v-card-text>
                                        <v-card-text v-if="userData.role==2">
                                            <b>Artist:</b> {{request.artist_user_id}}
                                            <b>Commission Type:</b> {{request.request_type == 1 ? 'Sculpture' : request.request_type == 2 ? 'Painting' : 'Other'}}
                                        </v-card-text>
                                    </v-card-item>
    
                                    <v-card-actions  v-if="userData.role==1">
                                        <v-btn color="success" @click="acceptCommissionRequest(request.id)">Accept</v-btn>
                                        <v-btn color="error" @click="declineCommissionRequest(request.id)">Decline</v-btn>
                                    </v-card-actions>
                                </v-card>
                            </v-col>
                        </v-row>
                    </v-card-text>
                </v-card-item>
            </v-card>

            <v-card class="mt-8">
                <v-card-item>
                    <v-card-title><b>Ongoing Commission Requests</b></v-card-title>

                    <v-card-item>
                        <v-card-text>
                            <v-row>
                                <v-col cols="4" v-for="request in ongoingCommissionRequests">
                                    <v-card>
                                        <v-card-item>
                                            <v-card-text v-if="userData.role==1">
                                                <b>Company:</b> {{request.requesting_user_id}}
                                                <b>Commission Type:</b> {{request.request_type == 1 ? 'Sculpture' : request.request_type == 2 ? 'Painting' : 'Other'}}
                                            </v-card-text>
                                            <v-card-text v-if="userData.role==2">
                                                <b>Artist:</b> {{request.artist_user_id}}
                                                <b>Commission Type:</b> {{request.request_type == 1 ? 'Sculpture' : request.request_type == 2 ? 'Painting' : 'Other'}}
                                            </v-card-text>
                                        </v-card-item>
                                    </v-card>
                                </v-col>
                            </v-row>
                        </v-card-text>
                    </v-card-item>
                </v-card-item>
            </v-card>
        </v-container>
    </v-container>
</template>

<script>
import CommissionRequestService from '@/services/CommissionRequestService';

export default {
    data: () => ({
        userData: JSON.parse(localStorage.getItem('userData')),
        pendingCommissionRequests: [],
        ongoingCommissionRequests: []
    }),
    async mounted() {
        this.$messaging.onMessage((payload) => {
            this.$store.commit('notiReceived');
            this.loadInitData();
        });
        await this.loadInitData();
    },
    methods: {
        async loadInitData() {
            const id = this.userData.id;
            this.pendingCommissionRequests = await CommissionRequestService.getPendingCommissionRequests(id);
            this.ongoingCommissionRequests = await CommissionRequestService.getOngoingCommissionRequests(id);
            console.log(this.$store.state.notiReceivedFlag);
        },
        async acceptCommissionRequest(id) {
            const resp = await CommissionRequestService.updateCommissionRequests(id, 2);
            this.loadInitData();
        },
        async declineCommissionRequest(id) {
            const resp = await CommissionRequestService.updateCommissionRequests(id, 3);
            this.loadInitData();
        }
    }
}
</script>