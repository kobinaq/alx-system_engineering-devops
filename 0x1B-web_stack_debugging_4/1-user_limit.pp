# 1-user_limit.pp
# Increase hard and soft file limits for the holberton user

exec { 'change-os-configuration-for-holberton-user':
  command => "sed -i '/holberton hard/d' /etc/security/limits.conf && \
              sed -i '/holberton soft/d' /etc/security/limits.conf && \
              echo 'holberton hard nofile 50000' >> /etc/security/limits.conf && \
              echo 'holberton soft nofile 50000' >> /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
