<template>
    <v-container fluid>
        <h1 class="text-center">Create Commission Request</h1>
        <v-container>
            <v-card>
                <v-card-item>
                    <v-card-title><b> Create a new Commission Request</b></v-card-title>
                </v-card-item>

                <v-card-text class="pa-4">
                    <v-row class="pa-4">
                        <p>Select an artist</p>
                    </v-row>
                    <v-row class="pa-4">
                        <v-card variant="outlined" v-for="artist in artists">
                            <v-card-title>Artista 1</v-card-title>
                        </v-card>
                    </v-row>

                    <v-row class="pa-4">
                        <label>Pick a commission type</label>
                    </v-row>
                    <v-row class="pa-4">
                        <v-select label="Commission Type..."
                        :items="commissionTypes"
                        item-value="id"
                        item-title="name"
                        v-model="selectedCommissionType"></v-select>
                    </v-row>
                </v-card-text>

                <v-row class="pa-4 px-8 pb-8">
                    <v-btn color="success" @click="createCommissionRequest()"><v-icon icon="mdi-plus"></v-icon> Create Commission Request</v-btn>
                </v-row>
            </v-card>
        </v-container>
    </v-container>
</template>

<script>
import UserService from '@/services/UserService';
import CommissionRequestService from '@/services/CommissionRequestService';

export default {
    data: () => ({
        artists: [],
        commissionTypes: [{id: 1, name: 'Sculpture'}, {id: 2, name: 'Painting'}, {id: 2, name: 'Other'}],
        selectedCommissionType: null,
    }),
    async mounted() {
        this.artists = await UserService.getAllArtists();
        console.log(this.artists);
    },
    methods: {
        async createCommissionRequest() {
            if (this.selectedCommissionType == null)
                return;
                console.log(this.selectedCommissionType);
            const resp = await CommissionRequestService.createCommissionRequests(1, 2, this.selectedCommissionType);
            console.log(resp);
        }
    }
}
</script>