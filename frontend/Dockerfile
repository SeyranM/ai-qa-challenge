FROM node:21-alpine AS build
WORKDIR /src
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine
COPY --from=build /src/dist /usr/share/nginx/html
