FROM node:20

WORKDIR /app

# Copy manifest files
COPY package.json package-lock.json* ./

# Install all dependencies (always)
RUN npm install

# Copy source code
COPY . .

# Expose port 3000 for Next.js
ENV PORT=3000
EXPOSE 3000

# Start Next.js in dev mode
CMD ["npm", "run", "dev", "--", "-p", "3000"]
FROM node:20

WORKDIR /app

# Copy manifest files
COPY package.json package-lock.json* ./

# Install all dependencies (always)
RUN npm install

# Copy source code
COPY . .

# Expose port 3000 for Next.js
ENV PORT=3000
EXPOSE 3000

# Start Next.js in dev mode
CMD ["npm", "run", "dev", "--", "-p", "3000"]
FROM node:20

WORKDIR /app

# Copy manifest files
COPY package.json package-lock.json* ./

# Install all dependencies (always)
RUN npm install

# Copy source code
COPY . .

# Expose port 3000 for Next.js
ENV PORT=3000
EXPOSE 3000

# Start Next.js in dev mode
CMD ["npm", "run", "dev", "--", "-p", "3000"]
