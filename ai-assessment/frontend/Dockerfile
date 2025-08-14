FROM node:20

WORKDIR /app

# Copy only package manifests first for better caching
COPY package.json package-lock.json* /app/

# Ensure Next.js + React are present even if package.json was missing them previously
RUN set -eux; \
    if ! grep -q '"next"' package.json; then \
      echo "Adding next/react/react-dom to package.json"; \
      npm install --save next react react-dom; \
    fi; \
    npm install

# Now copy the rest of the app
COPY . /app

ENV PORT=3000
# Explicitly expose so Codespaces can detect it
EXPOSE 3000

CMD ["npm", "run", "dev", "--", "-p", "3000"]
