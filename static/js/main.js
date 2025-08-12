// Main JavaScript for Student Management System

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Form validation enhancement
    initializeFormValidation();

    // Search functionality
    initializeSearch();

    // Table sorting
    initializeTableSorting();

    // Export functionality
    initializeExport();
});

// Form Validation
function initializeFormValidation() {
    const forms = document.querySelectorAll('form[novalidate]');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, select, textarea');
        
        inputs.forEach(input => {
            // Real-time validation
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            // Clear validation on input
            input.addEventListener('input', function() {
                clearFieldValidation(this);
            });
        });
        
        // Form submission validation
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showValidationMessage('Please correct the errors below.', 'danger');
            }
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';
    
    // Remove existing validation
    clearFieldValidation(field);
    
    // Required field validation
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required.';
    }
    
    // Email validation
    if (fieldName === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address.';
        }
    }
    
    // Phone validation
    if (fieldName === 'phone' && value) {
        const phoneRegex = /^[\+]?[0-9\s\-\(\)]+$/;
        if (!phoneRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid phone number.';
        }
    }
    
    // CGPA validation
    if (fieldName === 'cgpa' && value) {
        const cgpa = parseFloat(value);
        if (isNaN(cgpa) || cgpa < 0 || cgpa > 4) {
            isValid = false;
            errorMessage = 'CGPA must be between 0.00 and 4.00.';
        }
    }
    
    // Student ID validation
    if (fieldName === 'student_id' && value) {
        if (value.length < 3) {
            isValid = false;
            errorMessage = 'Student ID must be at least 3 characters long.';
        }
    }
    
    // Apply validation result
    if (!isValid) {
        showFieldError(field, errorMessage);
    }
    
    return isValid;
}

function clearFieldValidation(field) {
    field.classList.remove('is-invalid');
    const errorDiv = field.parentNode.querySelector('.invalid-feedback');
    if (errorDiv) {
        errorDiv.remove();
    }
}

function showFieldError(field, message) {
    field.classList.add('is-invalid');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback d-block';
    errorDiv.textContent = message;
    
    field.parentNode.appendChild(errorDiv);
}

function validateForm(form) {
    const inputs = form.querySelectorAll('input, select, textarea');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

// Search Functionality
function initializeSearch() {
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        let searchTimeout;
        
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                performSearch(this.value);
            }, 500);
        });
    }
}

function performSearch(query) {
    const currentUrl = new URL(window.location);
    currentUrl.searchParams.set('search', query);
    currentUrl.searchParams.delete('page'); // Reset to first page
    
    window.location.href = currentUrl.toString();
}

// Table Sorting
function initializeTableSorting() {
    const tableHeaders = document.querySelectorAll('th[data-sort]');
    
    tableHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const sortField = this.getAttribute('data-sort');
            const currentOrder = this.getAttribute('data-order') || 'asc';
            const newOrder = currentOrder === 'asc' ? 'desc' : 'asc';
            
            // Update all headers
            tableHeaders.forEach(h => h.setAttribute('data-order', ''));
            this.setAttribute('data-order', newOrder);
            
            // Update sort indicators
            tableHeaders.forEach(h => {
                h.classList.remove('sort-asc', 'sort-desc');
            });
            this.classList.add(`sort-${newOrder}`);
            
            // Perform sort
            sortTable(sortField, newOrder);
        });
    });
}

function sortTable(field, order) {
    const currentUrl = new URL(window.location);
    currentUrl.searchParams.set('sort', field);
    currentUrl.searchParams.set('order', order);
    currentUrl.searchParams.delete('page'); // Reset to first page
    
    window.location.href = currentUrl.toString();
}

// Export Functionality
function initializeExport() {
    const exportBtn = document.querySelector('.export-btn');
    if (exportBtn) {
        exportBtn.addEventListener('click', function(e) {
            e.preventDefault();
            exportData();
        });
    }
}

function exportData() {
    const currentUrl = new URL(window.location);
    currentUrl.searchParams.set('export', 'true');
    
    // Show loading state
    const btn = document.querySelector('.export-btn');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<span class="loading"></span> Exporting...';
    btn.disabled = true;
    
    fetch(currentUrl.toString())
        .then(response => response.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'students_export.csv';
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        })
        .catch(error => {
            console.error('Export failed:', error);
            showValidationMessage('Export failed. Please try again.', 'danger');
        })
        .finally(() => {
            btn.innerHTML = originalText;
            btn.disabled = false;
        });
}

// Utility Functions
function showValidationMessage(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Auto-hide after 5 seconds
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alertDiv);
        bsAlert.close();
    }, 5000);
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    });
}

function formatPhone(phone) {
    // Remove all non-digits
    const cleaned = phone.replace(/\D/g, '');
    
    // Format based on length
    if (cleaned.length === 10) {
        return `(${cleaned.slice(0, 3)}) ${cleaned.slice(3, 6)}-${cleaned.slice(6)}`;
    } else if (cleaned.length === 11 && cleaned[0] === '1') {
        return `+1 (${cleaned.slice(1, 4)}) ${cleaned.slice(4, 7)}-${cleaned.slice(7)}`;
    }
    
    return phone; // Return original if can't format
}

// AJAX Functions
function deleteStudent(studentId) {
    if (!confirm('Are you sure you want to delete this student?')) {
        return;
    }
    
    fetch(`/students/${studentId}/delete-ajax/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showValidationMessage(data.message, 'success');
            setTimeout(() => {
                location.reload();
            }, 1500);
        } else {
            showValidationMessage(data.message, 'danger');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showValidationMessage('An error occurred while deleting the student.', 'danger');
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Chart Functions (if Chart.js is loaded)
function initializeCharts() {
    if (typeof Chart !== 'undefined') {
        // Department Chart
        const deptCtx = document.getElementById('departmentChart');
        if (deptCtx) {
            new Chart(deptCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Computer Science', 'Information Technology', 'Electrical Engineering'],
                    datasets: [{
                        data: [30, 25, 20],
                        backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        }
        
        // Year Chart
        const yearCtx = document.getElementById('yearChart');
        if (yearCtx) {
            new Chart(yearCtx, {
                type: 'doughnut',
                data: {
                    labels: ['First Year', 'Second Year', 'Third Year', 'Fourth Year'],
                    datasets: [{
                        data: [35, 30, 25, 10],
                        backgroundColor: ['#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b']
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        }
    }
}

// Initialize charts when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeCharts();
});