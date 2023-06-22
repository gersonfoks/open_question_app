import {provide} from 'vue'

import {GradingService} from "@/service/GradingService";

const base_route = 'http://localhost:8000'

const gradingService = new GradingService(base_route)
export default function provideServices(app: any) {
    app.provide('gradingService', gradingService)
}

