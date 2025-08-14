FROM node:20

WORKDIR /app
COPY package.json package-lock.json* /app/
RUN npm install
COPY . /app

ENV PORT=3000
CMD ["npm", "run", "dev"]
