FROM node:lts-alpine as build-deps

WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn
COPY ./public/* ./public/
COPY ./src/* ./src/
RUN yarn build

FROM nginx:stable-alpine
COPY --from=build-deps /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
